def city_country(city, country, population = ''):
    formatted_city_country = city + ", " + country
    if population:
        formatted_city_country += " - population " + str(population)
    return formatted_city_country.title()
