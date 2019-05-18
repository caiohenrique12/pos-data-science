class CreateFileInputs < ActiveRecord::Migration[5.2]
  def change
    create_table :file_inputs do |t|
      t.string :name
      t.string :local
      t.references :user, foreign_key: true

      t.timestamps
    end
  end
end
