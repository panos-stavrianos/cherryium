import '/app/src/css/custom.css'

export function show_alert(message, color = 'primary') {
    let alert = {
        "content": {"icon": 'now-ui-icons ui-1_bell-53', "message": message},
        "options": {"type": color, "timer": 8000, "placement": {"from": "bottom", "align": "right"}}
    };
    $.notify(alert.content, alert.options)
}

$('#search').change(function () {
    console.log('on change')
    fetch('/search', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({search: $(this).val()})
    })
        .then((data) => data.text())
        .then((data) => {
            $('#search_results').html(data);
            $('#close_search_results').on('click', function () {
                $('#search_results_dropdown').removeClass('show')
            });
        })
        .catch((error) => console.error('Error:', error));
});


