require "application_system_test_case"

class FileInputsTest < ApplicationSystemTestCase
  setup do
    @file_input = file_inputs(:one)
  end

  test "visiting the index" do
    visit file_inputs_url
    assert_selector "h1", text: "File Inputs"
  end

  test "creating a File input" do
    visit file_inputs_url
    click_on "New File Input"

    fill_in "Local", with: @file_input.local
    fill_in "Name", with: @file_input.name
    fill_in "User", with: @file_input.user_id
    click_on "Create File input"

    assert_text "File input was successfully created"
    click_on "Back"
  end

  test "updating a File input" do
    visit file_inputs_url
    click_on "Edit", match: :first

    fill_in "Local", with: @file_input.local
    fill_in "Name", with: @file_input.name
    fill_in "User", with: @file_input.user_id
    click_on "Update File input"

    assert_text "File input was successfully updated"
    click_on "Back"
  end

  test "destroying a File input" do
    visit file_inputs_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "File input was successfully destroyed"
  end
end
