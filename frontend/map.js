function initMap() {
    // Map options
    var options = {
        center: {lat: 23.3441, lng: 85.3096}, // Coordinates for your location
        zoom: 15 // Zoom level (0 to 21)
    };

    // Create a new map
    var map = new google.maps.Map(document.getElementById('map'), options);

    // Add a marker for your location
    var marker = new google.maps.Marker({
        position: {lat: 23.3441, lng: 85.3096}, // Coordinates for your location
        map: map,
        title: "Yash's Eatery" // Marker title
    });
}
