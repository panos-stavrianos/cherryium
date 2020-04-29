import dt from 'datatables.net-bs4';
import {loader_hide, loader_show} from "./loader";

dt();

export function render() {
    $('#products').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/products_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {
                data: "name",
                render: function (data, type, row, meta) {
                    return `<a href="product/${row.id}">${row.name}</a>`;
                }
            },
            {data: "description"},
            {data: "price"},
            {
                data: "enabled",
                render: function (data, type, row, meta) {
                    return `<i class="far ${row.enabled ? 'fa-check-square' : 'fa-times-circle'} text-primary"></i>`;
                }
            }
        ]
    });
    $('#add_record').on('click', function () {
        let id = $(this).data('id')
        loader_show();
        fetch('/product_add_edit/' + id)
            .then((data) => data.text())
            .then((data) => {
                $('#add_edit_modal').html(data);
                $('#edit_modal').modal();
                loader_hide()
            })
            .catch((error) => console.error('Error:', error));
    });

}