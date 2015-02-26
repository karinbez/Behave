from behave import *
from selenium import webdriver


webdriver.Firefox().find_element_by_id('ng-campo-login').sendKeys('teclas')

webdr = webdriver
contr_brow = webdr.Firefox()
elemento = contr_brow.find_elemento_by_id('bolinha')
acao = elemento.sendKeys('teclas')


@given('acesso a tela de login')
def acesso_login(context):
	browser = webdriver.Firefox()
	browser.get('http://localhost:8080/nfe')
	
@when('logo como suporte')
def step_impl(context):
    browser.find_element_by_id('ng-campologin').sendKeys('suporte')
	browser.find_element_by_id('ng-camposenha').sendKeys('sup@2010')
	browser.find_element_by_id('ng-botaologin').click()

@then('verifico que acessei como suporte')
def step_impl(context):
    assert browser.find_element_by_id('ng-msg-boas').getText() == 'Bem vindo, suporte'