from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
        self.animal = Animal.objects.create(
            nome_cientifico = "Panthera leo",
            nome_popular = "Leão",
            predador = True,
            venenoso = False,
            domestico = False
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """Teste: se um usuário encontra um animal pesquisando."""
        home_page = self.browser.get(self.live_server_url + "/")
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual("Buscar animal", brand_element.text)
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute("placeholder"), "Exemplo: leão")
        buscar_animal_input.send_keys("leão")
        self.browser.find_element(By.CSS_SELECTOR, "form button").click()
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, ".result-description")
        self.assertGreater(len(caracteristicas), 3)