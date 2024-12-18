# LM Studio local server configuration
lmstudio_api_key = "" # Leave this empty for LM Studio
lmstudio_api_base = "http://localhost:1234/v1" # Using LM Studio standard local server
lmstudio_model_engine = "meta-llama-3-8b-instruct" # Replace this with the model you started the LM studio local server with for chat
lmstudio_text_embedding_model_engine = "text-embedding-nomic-embed-text-v1.5" # Replace this with the model you started the LM studio local server with for text embedding

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True