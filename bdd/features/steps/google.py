from behave import given, when, then

@given(u'que acessa a pagina do Google')
def step_impl(context):
    context.web.get("https://google.com")


@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element('xpath', "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    context.element.click()
    context.element.send_keys("base Corinthians")
    context.element.submit()

@when(u'pesquisa e realizada')
def step_impl(context):
    assert context.web.title == "base Corinthians - Pesquisa Google"

@then(u'o titulo da pagina deve ser validado')
def step_impl(context):
    pass