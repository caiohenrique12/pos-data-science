require 'test_helper'

class FileInputsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @file_input = file_inputs(:one)
  end

  test "should get index" do
    get file_inputs_url
    assert_response :success
  end

  test "should get new" do
    get new_file_input_url
    assert_response :success
  end

  test "should create file_input" do
    assert_difference('FileInput.count') do
      post file_inputs_url, params: { file_input: { local: @file_input.local, name: @file_input.name, user_id: @file_input.user_id } }
    end

    assert_redirected_to file_input_url(FileInput.last)
  end

  test "should show file_input" do
    get file_input_url(@file_input)
    assert_response :success
  end

  test "should get edit" do
    get edit_file_input_url(@file_input)
    assert_response :success
  end

  test "should update file_input" do
    patch file_input_url(@file_input), params: { file_input: { local: @file_input.local, name: @file_input.name, user_id: @file_input.user_id } }
    assert_redirected_to file_input_url(@file_input)
  end

  test "should destroy file_input" do
    assert_difference('FileInput.count', -1) do
      delete file_input_url(@file_input)
    end

    assert_redirected_to file_inputs_url
  end
end
