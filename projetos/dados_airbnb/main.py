from web_scraping import WebScraping

url = 'https://www.airbnb.com.br/s/S%C3%A3o-Paulo-~-S%C3%A3o-Paulo--Brasil/\
    homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week\
    &monthly_start_date=2023-08-01&monthly_length=3\
    &price_filter_input_type=0&price_filter_num_nights=4\
    &channel=EXPLORE&query=S%C3%A3o%20Paulo%20-%20S%C3%A3o%20Paulo&place_id=ChIJ9cXwmIFEzpQR7\
    -ebZCySXMo&date_picker_type=calendar&checkin=2023-08-07&checkout=2023-08-11&source\
    =structured_search_input_header&search_type=user_map_move&ne_lat=-23.51063790207311&ne_lng=-46.5864236019375&sw_lat=-23.6316760182516&sw_lng\
    =-46.7125335823288&zoom=12.567445256522486&zoom_level=12.567445256522486&search_by_map\
    =true'

web_scraping = WebScraping(url)

