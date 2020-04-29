import dt from 'datatables.net-bs4';
import {loader_hide, loader_show} from "./loader";

dt();

export function render() {
    $('#customers').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/customers_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {
                data: "name",
                render: function (data, type, row, meta) {
                    return `<a href="customer/${row.id}">${row.name}</a>`;
                }
            },
            {data: "phone_1"},
            {data: "phone_2"},
            {data: "comment"},
            {data: "sex", "visible": false, "searchable": false}
        ]
    });

    $('#add_record').on('click', function () {
        loader_show();
        fetch('/customer_add_edit/0')
            .then((data) => data.text())
            .then((data) => {
                $('#add_edit_modal').html(data);
                $('#edit_modal').modal();
                loader_hide()
            })
            .catch((error) => console.error('Error:', error));
    });
}