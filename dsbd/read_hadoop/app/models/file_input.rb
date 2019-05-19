class FileInput < ApplicationRecord
  belongs_to :user
  has_many_attached :local
end
