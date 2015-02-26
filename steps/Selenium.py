from selenium import webdriver

browser = webdriver.Firefox()

@given('acesso a pagina do facebook')
def abrir_pagina(context):
	browser.get("http://facebook.com")

@when('preencho o campo login')
def preencher_login(context):
	campo_login = browser.find_element_by_id('email')
	campo_login.send_keys('karin.bez@gmail.com')

@when('preencho o campo senha')
def preencher_senha(context):
	campo_senha = browser.find_element_by_id('pass')
	campo_senha.send_keys('senhazoada')

@when('clico em login')
def clicar_login(context):
	botao_entrar = browser.find_element_by_id('loginbutton')
	botao_entrar.click()

