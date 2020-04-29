import dtr from 'datatables.net-responsive-dt';
import dt from 'datatables.net-bs4';
import moment from 'moment';
import {loader_hide, loader_show} from "./loader";
import 'bootstrap-select/dist/js/bootstrap-select.min'
import 'bootstrap-select/dist/css/bootstrap-select.min.css'

dtr();
dt();

export function render() {
    $('#customer_products').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/customer_products_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {data: "customer_id", "visible": false, "searchable": false},
            {
                data: "customer_name",
                render: function (data, type, row, meta) {
                    return `<a href="customer/${row.customer_id}">${row.customer_name}</a>`;
                }
            },
            {data: "product_id", "visible": false, "searchable": false},
            {
                data: "product_name",
                render: function (data, type, row, meta) {
                    return `<a href="product/${row.product_id}">${row.product_name}</a>`;
                }
            },
            {data: "product_description"},
            {
                data: "created_at",
                render: function (data, type, row, meta) {
                    return moment(row.created_at).format('DD/MM/YYYY, hh:mm');
                }
            }
        ]
    });

    $('#customer_services').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/customer_services_data",
        columns: [
            {data: "id", "visible": false, "searchable": false},
            {data: "customer_id", "visible": false, "searchable": false},
            {
                data: "customer_name",
                render: function (data, type, row, meta) {
                    return `<a href="customer/${row.customer_id}">${row.customer_name}</a>`;
                }
            },
            {data: "service_id", "visible": false, "searchable": false},
            {
                data: "service_name",
                render: function (data, type, row, meta) {
                    return `<a href="service/${row.service_id}">${row.service_name}</a>`;
                }
            },
            {data: "service_description"},
            {
                data: "created_at",
                render: function (data, type, row, meta) {
                    return moment(row.created_at).format('DD/MM/YYYY, hh:mm');
                }
            }
        ]
    });

    $('#add_record').on('click', function () {
        loader_show();
        $('#edit_modal').modal();
        loader_hide()
    });
    fetch('/new_sale')
        .then((data) => data.text())
        .then((data) => {
            $('#add_edit_modal').html(data);
            $('.selectpicker').selectpicker({
                size: '10'
            });
            $('#add_record_icon').removeClass("fa fa-spinner fa-spin").addClass("fas fa-plus")
        })
        .catch((error) => console.error('Error:', error));
}