from page.page_manager import(
  pre_page,
  login_page,
  main_page,
  profile_page
)
from test_data.yaml_data import YamlData

def test_act(yaml_data: YamlData):
    pre_page.click_login()
    login_page.login_act(yaml_data.email, yaml_data.pwd)
    main_page.open_edit_profile()
    profile_page.set_up_birthday()
