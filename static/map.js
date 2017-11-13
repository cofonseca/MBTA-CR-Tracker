document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelectorAll('#map').length > 0) {  
        var js_file = document.createElement('script');
        js_file.type = 'text/javascript';
        js_file.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyB55F1-KNurF3fVzoeUjJoSkVUIALSY_KA&callback=initMap';
        document.getElementsByTagName('head')[0].appendChild(js_file);
    }
});
    
function initMap() {
    var lat = parseFloat(document.getElementById('map').dataset.lat)
    var lng = parseFloat((document.getElementById('map').dataset.lon).split(' ')[1])
    coords = {lat: lat, lng: lng}
    console.log(coords)
    map = new google.maps.Map(document.getElementById('map'), {
        center: coords,
        zoom: 18
    });
    var marker = new google.maps.Marker({
        position: coords,
        map: map
      });
}