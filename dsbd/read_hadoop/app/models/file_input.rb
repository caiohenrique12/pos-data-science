class FileInput < ApplicationRecord
  belongs_to :user
  attr_accessor :file

  def mv_file_tmp original_path, file_name
    new_file_name    = original_path.path.gsub(/([\/tmp])/, "")
    new_folder_name  = file_name.split(".").first
    new_input_folder = Rails.root + "/tmp/#{new_folder_name}"

    unless File.directory? new_input_folder
      FileUtils.mkdir(new_input_folder)
    end

    self.update(local_file: new_input_folder)

    FileUtils.cp original_path, new_input_folder

    initialize_hadoop_hdfs new_file_name
  end

  def initialize_hadoop_hdfs path_file
    hadoop_path = "/home/dev/Documentos/hadoop-2.9.1"

    system "#{hadoop_path}/bin/"
  end
end
