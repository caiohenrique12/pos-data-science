require 'fileutils'

namespace :hadoop do
  desc 'create input folder and processing map reduce hadoop example'
  task :create_input_folder => :environment do
    root_path = "/home/dev"
    test_path = "/home/dev/tmp"
    hadoop_path = root_path + "/Documentos/hadoop-2.9.1"

    unless File.directory? test_path
      FileUtils.mkdir('/home/dev/tmp')
      FileUtils.mkdir('/home/dev/tmp/input')
    end

    puts "Copiando arquivos do hadoop para input"
    system "cp #{hadoop_path}/etc/hadoop/*.xml #{root_path}/tmp/input"
    puts "executando map reduce de exmplo"
    system "#{hadoop_path}/bin/hadoop jar #{hadoop_path}/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.1.jar grep #{test_path}/input #{test_path}/output 'dfs[a-z.]+'"
    # FileUtils.cp_r(hadoop_path + "/etc/hadoop/*.xml", root_path + "/tmp/input/")
  end
end
