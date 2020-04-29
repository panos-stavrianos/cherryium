import dt from 'datatables.net-bs4';
import {loader_hide, loader_show} from "./loader";

dt();

export function render() {
    $('#services').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/services_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {
                data: "name",
                render: function (data, type, row, meta) {
                    return `<a href="service/${row.id}">${row.name}</a>`;
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
        fetch('/service_add_edit/' + id)
            .then((data) => data.text())
            .then((data) => {
                $('#add_edit_modal').html(data);
                $('#edit_modal').modal();
                loader_hide()
            })
            .catch((error) => console.error('Error:', error));
    });
}