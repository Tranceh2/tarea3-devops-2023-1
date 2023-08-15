import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestMoviesApp:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def adddirector(self, director):
        self.driver.get("http://localhost:8001/")
        self.driver.set_window_size(1920, 2135)
        self.driver.find_element(By.ID, ":r1:-tab-1").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys(director)
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

    def addmovie(self, director, title, description, year):
        self.driver.get("http://localhost:8001/")
        self.driver.set_window_size(1920, 2135)
        self.driver.find_element(By.CSS_SELECTOR, "#add-movie-btn .w-16").click()
        self.driver.find_element(By.ID, "title").click()
        self.driver.find_element(By.ID, "title").send_keys(title)
        self.driver.find_element(By.ID, "description").click()
        self.driver.find_element(By.ID, "description").send_keys(description)
        self.driver.find_element(By.ID, "year").click()
        self.driver.find_element(By.ID, "year").send_keys(year)
        self.driver.find_element(By.ID, "director_id").click()
        dropdown = self.driver.find_element(By.ID, "director_id")
        dropdown.find_element(By.XPATH, "//option[. = '"+director+"']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()

directors = ["Stanley Kubrick", "Wes Anderson"]
movies = [
    ("Stanley Kubrick", "2001: A Space Odyssey", "La supercomputadora HAL 9000 guía a un equipo de tres astronautas en un viaje en el que buscan descubrir los orígenes de la humanidad.", "1968"),
    ("Wes Anderson", "Isle of Dogs", "El alcalde de una ciudad japonesa decreta que, con motivo de una epidemia de gripe canina, todos los perros deben quedar confinados en una isla. Un niño de 12 años emprende una aventura para llegar hasta la isla y rescatar a su mascota.", "2018"),
    ("Cristopher Nolan", "Inception", "Dom Cobb (Leonardo DiCaprio) es un ladrón con una extraña habilidad para entrar a los sueños de la gente y robarle los secretos de sus subconscientes. Su habilidad lo ha convertido en un atractivo en el mundo del espionaje corporativo, pero ha tenido un gran costo en la gente que ama.", "2010"),
    ("Cristopher Nolan", "Tenet", "Un agente secreto emprende una misión que se desarrolla más allá del tiempo real, para intentar prevenir una Tercera Guerra Mundial.", "2020")
]

@pytest.mark.parametrize("director", directors)
def test_adddirector(director):
    app = TestMoviesApp()
    app.setup_method()
    app.adddirector(director)
    app.teardown_method()

@pytest.mark.parametrize("director, title, description, year", movies)
def test_addmovie(director, title, description, year):
    app = TestMoviesApp()
    app.setup_method()
    app.addmovie(director, title, description, year)
    app.teardown_method()
