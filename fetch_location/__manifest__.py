{
    'name': 'Fetch Location',
    'category': 'Location',
    'version': '16.0.0.0.6',
    "author" : "Midaad Company",
    'website': "https://midaad.com/",
    'description': """
        Google Map Location,\nThis module create widget Google Map that allow
        you to get your coordinates (longitude and latitude) and with a button 
        (Get My Current Coordinate). 
        To use this module go to your module and Create 2 new fields 'Float' 
        with name (provider_latitude, provider_longitude) and 1 field Boolean 
        with name (is_today) to check if your date is today or not to use the 
        widget if you do not need to use condition of 'is_today' just make the 
        field and put default value True, in your xml file you can create 
        <widget type="location_ci"/> and once you click the button (Get my 
        current coordinate) widget capture your long and lat into your fields
    """,
    'depends': ['hr', 'base', 'web'],
    'license': 'AGPL-3',
    'data': [
        'views/work_location.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'fetch_location/static/src/js/current_coordinates.js',
            'fetch_location/static/src/xml/coordinates_template.xml',
        ],
    },
    'installable': True,
    'images': [
        'static/description/Googlemap.jpg',
    ],


}
