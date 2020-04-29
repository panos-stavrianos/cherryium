import {loader_hide, loader_show} from "./loader";

export function render() {
    $('#edit_record').on('click', function () {
        let id = $(this).data('id')
        loader_show();
        fetch('/partner_add_edit/' + id)
            .then((data) => data.text())
            .then((data) => {
                $('#add_edit_modal').html(data);
                $('#edit_modal').modal();
                loader_hide()
            })
            .catch((error) => console.error('Error:', error));
    });
}