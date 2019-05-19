class FileInputsController < ApplicationController
  before_action :set_file_input, only: [:show, :edit, :update, :destroy]

  # GET /file_inputs
  # GET /file_inputs.json
  def index
    @file_inputs = FileInput.all
  end

  # GET /file_inputs/1
  # GET /file_inputs/1.json
  def show
  end

  # GET /file_inputs/new
  def new
    @file_input = FileInput.new
  end

  # GET /file_inputs/1/edit
  def edit
  end

  # POST /file_inputs
  # POST /file_inputs.json
  def create
    @file_input = FileInput.new(file_input_params)
    @file_input.user_id = current_user.id

    respond_to do |format|
      if @file_input.save
        @file_input.mv_file_tmp(params[:file_input][:file].tempfile, params[:file_input][:file].original_filename)
        format.html { redirect_to file_inputs_path, notice: 'File was successfully created.' }
        format.json { render :show, status: :created, location: @file_input }
      else
        format.html { render :new }
        format.json { render json: @file_input.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /file_inputs/1
  # PATCH/PUT /file_inputs/1.json
  def update
    respond_to do |format|
      if @file_input.update(file_input_params)
        format.html { redirect_to file_inputs_path, notice: 'File was successfully updated.' }
        format.json { render :show, status: :ok, location: @file_input }
      else
        format.html { render :edit }
        format.json { render json: @file_input.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /file_inputs/1
  # DELETE /file_inputs/1.json
  def destroy
    @file_input.destroy
    respond_to do |format|
      format.html { redirect_to file_inputs_url, notice: 'File was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_file_input
      @file_input = FileInput.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def file_input_params
      params.require(:file_input).permit(:name, :user_id, :file)
    end
end
