from bfcl.model_handler.api_inference.claude import ClaudeHandler
from bfcl.model_handler.api_inference.cohere import CohereHandler
from bfcl.model_handler.api_inference.databricks import DatabricksHandler
from bfcl.model_handler.api_inference.deepseek import DeepSeekAPIHandler
from bfcl.model_handler.api_inference.fireworks import FireworksHandler
from bfcl.model_handler.api_inference.functionary import FunctionaryHandler
from bfcl.model_handler.api_inference.gemini import GeminiHandler
from bfcl.model_handler.api_inference.gogoagent import GoGoAgentHandler
from bfcl.model_handler.api_inference.gorilla import GorillaHandler
from bfcl.model_handler.api_inference.grok import GrokHandler
from bfcl.model_handler.api_inference.mistral import MistralHandler
from bfcl.model_handler.api_inference.nexus import NexusHandler
from bfcl.model_handler.api_inference.nova import NovaHandler
from bfcl.model_handler.api_inference.novita import NovitaHandler
from bfcl.model_handler.api_inference.nvidia import NvidiaHandler
from bfcl.model_handler.api_inference.openai import OpenAIHandler
from bfcl.model_handler.api_inference.writer import WriterHandler
from bfcl.model_handler.api_inference.yi import YiHandler
from bfcl.model_handler.local_inference.bielik import BielikHandler
from bfcl.model_handler.local_inference.deepseek import DeepseekHandler
from bfcl.model_handler.local_inference.deepseek_coder import DeepseekCoderHandler
from bfcl.model_handler.local_inference.deepseek_reasoning import DeepseekReasoningHandler
from bfcl.model_handler.local_inference.falcon_fc import Falcon3FCHandler
from bfcl.model_handler.local_inference.gemma import GemmaHandler
from bfcl.model_handler.local_inference.glaive import GlaiveHandler
from bfcl.model_handler.local_inference.glm import GLMHandler
from bfcl.model_handler.local_inference.granite import GraniteHandler
from bfcl.model_handler.local_inference.hammer import HammerHandler
from bfcl.model_handler.local_inference.hermes import HermesHandler
from bfcl.model_handler.local_inference.llama import LlamaHandler
from bfcl.model_handler.local_inference.llama_3_1 import LlamaHandler_3_1
from bfcl.model_handler.local_inference.minicpm import MiniCPMHandler
from bfcl.model_handler.local_inference.minicpm_fc import MiniCPMFCHandler
from bfcl.model_handler.local_inference.mistral_fc import MistralFCHandler
from bfcl.model_handler.local_inference.think_agent import ThinkAgentHandler
from bfcl.model_handler.local_inference.phi import PhiHandler
from bfcl.model_handler.local_inference.phi_fc import PhiFCHandler
from bfcl.model_handler.local_inference.quick_testing_oss import QuickTestingOSSHandler
from bfcl.model_handler.local_inference.qwen import QwenHandler
from bfcl.model_handler.local_inference.qwen_fc import QwenFCHandler
from bfcl.model_handler.local_inference.salesforce_llama import SalesforceLlamaHandler
from bfcl.model_handler.local_inference.salesforce_qwen import SalesforceQwenHandler
from bfcl.model_handler.api_inference.mining import MiningHandler

# TODO: Add meta-llama/Llama-3.1-405B-Instruct

# Inference through API calls
api_inference_handler_map = {
    "gorilla-openfunctions-v2": GorillaHandler,
    "DeepSeek-R1": DeepSeekAPIHandler,
    "DeepSeek-V3-FC": DeepSeekAPIHandler,
    "gpt-4.5-preview-2025-02-27": OpenAIHandler,
    "gpt-4.5-preview-2025-02-27-FC": OpenAIHandler,
    "gpt-4.1-2025-04-14-FC": OpenAIHandler,
    "gpt-4.1-2025-04-14": OpenAIHandler,
    "gpt-4.1-mini-2025-04-14-FC": OpenAIHandler,
    "gpt-4.1-mini-2025-04-14": OpenAIHandler,
    "gpt-4.1-nano-2025-04-14-FC": OpenAIHandler,
    "gpt-4.1-nano-2025-04-14": OpenAIHandler,
    "o1-2024-12-17-FC": OpenAIHandler,
    "o1-2024-12-17": OpenAIHandler,
    "o3-mini-2025-01-31-FC": OpenAIHandler,
    "o3-mini-2025-01-31": OpenAIHandler,
    "gpt-4o-2024-11-20": OpenAIHandler,
    "gpt-4o-2024-11-20-FC": OpenAIHandler,
    "gpt-4o-mini-2024-07-18": OpenAIHandler,
    "gpt-4o-mini-2024-07-18-FC": OpenAIHandler,
    "o4-mini-2025-04-16-FC": OpenAIHandler,
    "o4-mini-2025-04-16": OpenAIHandler,
    "claude-3-opus-20240229": ClaudeHandler,
    "claude-3-opus-20240229-FC": ClaudeHandler,
    "claude-3-7-sonnet-20250219": ClaudeHandler,
    "claude-3-7-sonnet-20250219-FC": ClaudeHandler,
    "claude-3-5-sonnet-20241022": ClaudeHandler,
    "claude-3-5-sonnet-20241022-FC": ClaudeHandler,
    "claude-3-5-haiku-20241022": ClaudeHandler,
    "claude-3-5-haiku-20241022-FC": ClaudeHandler,
    "nova-pro-v1.0": NovaHandler,
    "nova-lite-v1.0": NovaHandler,
    "nova-micro-v1.0": NovaHandler,
    "open-mistral-nemo-2407": MistralHandler,
    "open-mistral-nemo-2407-FC": MistralHandler,
    "mistral-large-2411": MistralHandler,
    "mistral-large-2411-FC": MistralHandler,
    "mistral-small-2503": MistralHandler,
    "mistral-small-2503-FC": MistralHandler,
    "firefunction-v2-FC": FireworksHandler,
    "Nexusflow-Raven-v2": NexusHandler,
    "gemini-2.0-flash-lite-001-FC": GeminiHandler,
    "gemini-2.0-flash-lite-001": GeminiHandler,
    "gemini-2.0-flash-001-FC": GeminiHandler,
    "gemini-2.0-flash-001": GeminiHandler,
    "gemini-2.5-pro-exp-03-25-FC": GeminiHandler,
    "gemini-2.5-pro-exp-03-25": GeminiHandler,
    "gemini-2.0-flash-thinking-exp-01-21": GeminiHandler,
    "meetkai/functionary-small-v3.1-FC": FunctionaryHandler,
    "meetkai/functionary-medium-v3.1-FC": FunctionaryHandler,
    "databricks-dbrx-instruct": DatabricksHandler,
    "command-r-plus-FC": CohereHandler,
    "command-r7b-12-2024-FC": CohereHandler,
    "command-a-03-2025-FC": CohereHandler,
    "snowflake/arctic": NvidiaHandler,
    "nvidia/nemotron-4-340b-instruct": NvidiaHandler,
    "BitAgent/GoGoAgent": GoGoAgentHandler,
    # "yi-large-fc": YiHandler,  #  Their API is under maintenance, and will not be back online in the near future
    "palmyra-x-004": WriterHandler,
    "grok-3-beta-FC": GrokHandler,
    "grok-3-beta": GrokHandler,
    "grok-3-mini-beta-FC": GrokHandler,
    "grok-3-mini-beta": GrokHandler,
    "xiaoming-14B": MiningHandler,
}

# Inference through local hosting
local_inference_handler_map = {
    "deepseek-ai/DeepSeek-R1": DeepseekReasoningHandler,  # This is the local version of DeepSeek-R1
    "google/gemma-3-1b-it": GemmaHandler,
    "google/gemma-3-4b-it": GemmaHandler,
    "google/gemma-3-12b-it": GemmaHandler,
    "google/gemma-3-27b-it": GemmaHandler,
    "meta-llama/Llama-3.1-8B-Instruct-FC": LlamaHandler_3_1,
    "meta-llama/Llama-3.1-8B-Instruct": LlamaHandler,
    "meta-llama/Llama-3.1-70B-Instruct-FC": LlamaHandler_3_1,
    "meta-llama/Llama-3.1-70B-Instruct": LlamaHandler,
    "meta-llama/Llama-3.2-1B-Instruct-FC": LlamaHandler,
    "meta-llama/Llama-3.2-3B-Instruct-FC": LlamaHandler,
    "meta-llama/Llama-3.3-70B-Instruct-FC": LlamaHandler,
    "meta-llama/Llama-4-Scout-17B-16E-Instruct-FC": LlamaHandler,
    "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8-FC": LlamaHandler,
    "Salesforce/Llama-xLAM-2-70b-fc-r": SalesforceLlamaHandler,
    "Salesforce/Llama-xLAM-2-8b-fc-r": SalesforceLlamaHandler,
    "Salesforce/xLAM-2-32b-fc-r": SalesforceQwenHandler,
    "Salesforce/xLAM-2-3b-fc-r": SalesforceQwenHandler,
    "Salesforce/xLAM-2-1b-fc-r": SalesforceQwenHandler,
    "mistralai/Ministral-8B-Instruct-2410": MistralFCHandler,
    "microsoft/phi-4": PhiHandler,
    "microsoft/Phi-4-mini-instruct": PhiHandler,
    "microsoft/Phi-4-mini-instruct-FC": PhiFCHandler,
    "ibm-granite/granite-20b-functioncalling": GraniteHandler,
    "MadeAgents/Hammer2.1-7b": HammerHandler,
    "MadeAgents/Hammer2.1-3b": HammerHandler,
    "MadeAgents/Hammer2.1-1.5b": HammerHandler,
    "MadeAgents/Hammer2.1-0.5b": HammerHandler,
    "THUDM/glm-4-9b-chat": GLMHandler,
    "Qwen/Qwen2.5-0.5B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-0.5B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-1.5B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-1.5B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-3B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-3B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-7B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-7B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-14B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-14B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-32B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-32B-Instruct": QwenHandler,
    "Qwen/Qwen2.5-72B-Instruct-FC": QwenFCHandler,
    "Qwen/Qwen2.5-72B-Instruct": QwenHandler,
    "Team-ACE/ToolACE-2-8B": LlamaHandler,
    "openbmb/MiniCPM3-4B": MiniCPMHandler,
    "openbmb/MiniCPM3-4B-FC": MiniCPMFCHandler,
    "watt-ai/watt-tool-8B": LlamaHandler,
    "watt-ai/watt-tool-70B": LlamaHandler,
    "ZJared/Haha-7B": QwenHandler,
    "speakleash/Bielik-11B-v2.3-Instruct": BielikHandler,
    "NovaSky-AI/Sky-T1-32B-Preview": QwenHandler,
    "Qwen/QwQ-32B-Preview": QwenHandler,
    "tiiuae/Falcon3-10B-Instruct-FC": Falcon3FCHandler,
    "tiiuae/Falcon3-7B-Instruct-FC": Falcon3FCHandler,
    "tiiuae/Falcon3-3B-Instruct-FC": Falcon3FCHandler,
    "tiiuae/Falcon3-1B-Instruct-FC": Falcon3FCHandler,
    "uiuc-convai/CoALM-8B": LlamaHandler,
    "uiuc-convai/CoALM-70B": LlamaHandler,
    "uiuc-convai/CoALM-405B": LlamaHandler,
    "BitAgent/BitAgent-8B": LlamaHandler,
    "ThinkAgents/ThinkAgent-1B": ThinkAgentHandler,
}

# Inference through third-party inference platforms for open-source models
third_party_inference_handler_map = {
    # Novita AI
    "meta-llama/llama-4-maverick-17b-128e-instruct-fp8-novita": NovitaHandler,
    "meta-llama/llama-4-maverick-17b-128e-instruct-fp8-FC-novita": NovitaHandler,
    "meta-llama/llama-4-scout-17b-16e-instruct-novita": NovitaHandler,
    "meta-llama/llama-4-scout-17b-16e-instruct-FC-novita": NovitaHandler,
    "qwen/qwq-32b-FC-novita": NovitaHandler,
    "qwen/qwq-32b-novita": NovitaHandler,
}

# Deprecated/outdated models, no longer on the leaderboard
outdated_model_handler_map = {
    # "gorilla-openfunctions-v0": GorillaHandler,
    # "o1-preview-2024-09-12": OpenAIHandler,
    # "o1-mini-2024-09-12": OpenAIHandler,
    # "gpt-4o-2024-08-06": OpenAIHandler,
    # "gpt-4o-2024-08-06-FC": OpenAIHandler,
    # "gpt-4o-2024-05-13": OpenAIHandler,
    # "gpt-4o-2024-05-13-FC": OpenAIHandler,
    # "gpt-4-1106-preview-FC": OpenAIHandler,
    # "gpt-4-1106-preview": OpenAIHandler,
    # "gpt-4-0125-preview-FC": OpenAIHandler,
    # "gpt-4-0125-preview": OpenAIHandler,
    # "gpt-4-0613-FC": OpenAIHandler,
    # "gpt-4-0613": OpenAIHandler,
    # "gpt-4-turbo-2024-04-09": OpenAIHandler,
    # "gpt-4-turbo-2024-04-09-FC": OpenAIHandler,
    # "gpt-3.5-turbo-0125": OpenAIHandler,
    # "gpt-3.5-turbo-0125-FC": OpenAIHandler,
    # "claude-2.1": ClaudeHandler,
    # "claude-instant-1.2": ClaudeHandler,
    # "claude-3-sonnet-20240229": ClaudeHandler,
    # "claude-3-sonnet-20240229-FC": ClaudeHandler,
    # "claude-3-5-sonnet-20240620": ClaudeHandler,
    # "claude-3-5-sonnet-20240620-FC": ClaudeHandler,
    # "claude-3-haiku-20240307": ClaudeHandler,
    # "claude-3-haiku-20240307-FC": ClaudeHandler,
    # "deepseek-ai/DeepSeek-V2.5": DeepseekCoderHandler,
    # "deepseek-ai/DeepSeek-Coder-V2-Instruct-0724": DeepseekCoderHandler,
    # "deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct": DeepseekCoderHandler,
    # "deepseek-ai/DeepSeek-V2-Chat-0628": DeepseekHandler,
    # "deepseek-ai/DeepSeek-V2-Lite-Chat": DeepseekHandler,
    # "firefunction-v1-FC": FireworksHandler,
    # "gemini-2.0-pro-exp-02-05-FC": GeminiHandler,
    # "gemini-2.0-pro-exp-02-05": GeminiHandler,
    # "gemini-1.5-pro-002": GeminiHandler,
    # "gemini-1.5-pro-002-FC": GeminiHandler,
    # "gemini-1.5-pro-001": GeminiHandler,
    # "gemini-1.5-pro-001-FC": GeminiHandler,
    # "gemini-1.5-flash-002": GeminiHandler,
    # "gemini-1.5-flash-002-FC": GeminiHandler,
    # "gemini-1.5-flash-001": GeminiHandler,
    # "gemini-1.5-flash-001-FC": GeminiHandler,
    # "gemini-1.0-pro-002": GeminiHandler,
    # "gemini-1.0-pro-002-FC": GeminiHandler,
    # "gemini-1.0-pro-001": GeminiHandler,
    # "gemini-1.0-pro-001-FC": GeminiHandler,
    # "Qwen/Qwen2-1.5B-Instruct": QwenHandler,
    # "Qwen/Qwen2-7B-Instruct": QwenHandler,
    # "meetkai/functionary-small-v3.1-FC": FunctionaryHandler,
    # "open-mixtral-8x22b": MistralHandler,
    # "open-mixtral-8x22b-FC": MistralHandler,
    # "open-mixtral-8x7b": MistralHandler,
    # "mistral-large-2407": MistralHandler,
    # "mistral-large-2407-FC": MistralHandler,
    # "mistral-medium-2312": MistralHandler,
    # "mistral-small-2402": MistralHandler,
    # "mistral-small-2402-FC": MistralHandler,
    # "mistral-tiny-2312": MistralHandler,
    # "meta-llama/Meta-Llama-3-8B-Instruct-FC": LlamaHandler,
    # "meta-llama/Meta-Llama-3-70B-Instruct-FC": LlamaHandler,
    # "microsoft/Phi-3-mini-4k-instruct": PhiHandler,
    # "microsoft/Phi-3-mini-128k-instruct": PhiHandler,
    # "microsoft/Phi-3-small-8k-instruct": PhiHandler,
    # "microsoft/Phi-3-small-128k-instruct": PhiHandler,
    # "microsoft/Phi-3-medium-4k-instruct": PhiHandler,
    # "microsoft/Phi-3-medium-128k-instruct": PhiHandler,
    # "microsoft/Phi-3.5-mini-instruct": PhiHandler,
    # "NousResearch/Hermes-2-Pro-Mistral-7B": HermesHandler,
    # "NousResearch/Hermes-2-Pro-Llama-3-8B": HermesHandler,
    # "NousResearch/Hermes-2-Theta-Llama-3-8B": HermesHandler,
    # "NousResearch/Hermes-2-Pro-Llama-3-70B": HermesHandler,
    # "NousResearch/Hermes-2-Theta-Llama-3-70B": HermesHandler,
    # "Team-ACE/ToolACE-8B": LlamaHandler,
    # "glaiveai/glaive-function-calling-v1": GlaiveHandler,
    # "google/gemma-7b-it": GemmaHandler,
    # "deepseek-ai/deepseek-coder-6.7b-instruct": DeepseekHandler,
    # "grok-beta": GrokHandler,
}

HANDLER_MAP = {**api_inference_handler_map, **local_inference_handler_map, **third_party_inference_handler_map}
