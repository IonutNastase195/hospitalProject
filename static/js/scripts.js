function initMap() {
    // Generate random latitude and longitude within the range of cities
    let latitude = (Math.random() * (85 - (-85)) + (-85)).toFixed(6); // Limit latitude range to -85 to 85 to avoid polar regions
    let longitude = (Math.random() * (180 - (-180)) + (-180)).toFixed(6); // Longitude range is -180 to 180

    // Create a map centered at the random location
    let map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: parseFloat(latitude), lng: parseFloat(longitude)},
        zoom: 10
    });

    // Add a marker at the random location
    let marker = new google.maps.Marker({
        position: {lat: parseFloat(latitude), lng: parseFloat(longitude)},
        map: map
    });
}
