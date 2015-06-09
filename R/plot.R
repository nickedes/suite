library(plotly)

# Learn about API authentication here: https://plot.ly/r/getting-started
# Find your api_key here: https://plot.ly/settings/api

py <- plotly()

m <- ggplot(movies, aes(x=rating)) +
        geom_histogram(aes(weight = votes))

out <- py$ggplotly(m, kwargs=list(filename="../data/AirPassengers.csv"))

plotly_url <- out$response$url
