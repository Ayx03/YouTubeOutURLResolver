import urllib.parse

url = "https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnpXcUZ1bEhLU3R6WWw5dnRNclBQTHVnaGhaQXxBQ3Jtc0treU9oV1l6R1Y2cnVybWlMc011Si1aWktWaHQ4cEFFU0c2dDBxNFRoOXJvNFBiM2hnOUNIQjd3WjJ5TjFUT2hWbHFhX2lIX3VOaVhWRWhVM216Slo3a201RWJuVjBWT3BHaFEyRERGcVY0aVk4SFVMRQ&q=https%3A%2F%2Fmusic.apple.com%2Fjp%2Fartist%2F%25E5%25AE%25B6%25E3%2581%25AE%25E8%25A3%258F%25E3%2581%25A7%25E3%2583%259E%25E3%2583%25B3%25E3%2583%259C%25E3%2582%25A6%25E3%2581%258C%25E6%25AD%25BB%25E3%2582%2593%25E3%2581%25A7%25E3%2582%258Bp%2F399362402&v=avfzmofxzig"

parsed_url = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)

target_url = parsed_url['q'][0]

print(target_url)
