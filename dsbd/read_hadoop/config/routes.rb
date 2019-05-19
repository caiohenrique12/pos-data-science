Rails.application.routes.draw do
  resources :file_inputs, except: [:show, :destroy]
  devise_for :users
  root to: 'file_inputs#index'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
