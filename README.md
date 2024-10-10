## UK 2023 MOT Failure Rate by Postcode Area
This is a simple shiny app that produces an interactive map and let's exploring UK MOT failure rates by the postcode area. There is a simple drawdown option that let's modifying map output by the vehicle age.

### App demo: ![](https://github.com/ASemeyutin/MOT_FRate_2023/blob/main/app_demo.gif)
While app is also avialable [here](https://asemeyutin.shinyapps.io/motfr2023/), it is recommended that it is run locally. This is just a small experiment that preceeds a different project and this link will become inactive in the future. If requirements are satisfied it may require shinylive to run on Github (without deployment) or VS Code shiny extension if run using python on your machine.
\vspace{10cm}
FR23.csv was produced using open access [Anonymised UK MOT tests data for 2023](https://www.data.gov.uk/dataset/e3939ef8-30c7-4ca8-9c7c-ad9475cc9b2f/anonymised-mot-tests-and-results), while postcode-boundaries.geojson was coverted from the open access [KLM](https://www.freemaptools.com/uk-postcode-map.htm) file.
