import dt from 'datatables.net-bs4';
import {loader_hide, loader_show} from "./loader";

dt();

export function render() {
    $('#expenses').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/expenses_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {
                data: "name",
                render: function (data, type, row, meta) {
                    return `<a href="expense/${row.id}">${row.name}</a>`;
                }
            },
            {data: "price"}
        ]
    });
    $('#add_record').on('click', function () {
        let id = $(this).data('id')
        loader_show();
        fetch('/expense_add_edit/' + id)
            .then((data) => data.text())
            .then((data) => {
                $('#add_edit_modal').html(data);
                $('#edit_modal').modal();
                loader_hide()
            })
            .catch((error) => console.error('Error:', error));
    });
}