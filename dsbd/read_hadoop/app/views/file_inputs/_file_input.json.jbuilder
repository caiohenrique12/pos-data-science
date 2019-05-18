json.extract! file_input, :id, :name, :local, :user_id, :created_at, :updated_at
json.url file_input_url(file_input, format: :json)
