function updateData(locations, image) {
    let dataContainer = document.getElementById("data_container")
    let imageContainer = document.getElementById("image")

    let locations_HTML = ""

    locations.forEach((location) => locations_HTML += `<p>▸ ${location}</p>`)

    dataContainer.innerHTML = locations_HTML
    imageContainer.src = `data:image/png;base64,${image}`
}

function fetchData() {
    let xhr = new XMLHttpRequest()
    xhr.open("GET", "/api/get_active", true)

    xhr.onload = function () {
        if (xhr.status === 200) {
            let response = JSON.parse(xhr.responseText)

            let locations = response["locations"]
            let image = response["image"]

            updateData(locations, image)
        }
    }

    xhr.send()
}