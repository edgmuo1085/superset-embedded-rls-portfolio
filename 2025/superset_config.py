import os
import logging
from datetime import timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("⚡ Config personalizada cargada ⚡")

### IMPRIMIR VARIABLES DE ENTORNO   
logger.info("SUPERSET_SECRET_KEY: %s",      os.environ.get("SUPERSET_SECRET_KEY", "default_inseguro_cambiar"))
logger.info("SUPERSET_JWT_SECRET: %s",      os.environ.get("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar"))
logger.info("SUPERSET_SQLALCHEMY_DATABASE_URI: %s", os.environ.get("SUPERSET_SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://superset:superset@db:5432/superset"))


# ==============================
# 🔑 Claves seguras desde variables de entorno
# ==============================
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "default_inseguro_cambiar")
JWT_SECRET = os.getenv("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar")

# --- Settings for Embedding & Guest Tokens ---
# ENABLE_EMBEDDED_SUPERSET is controlled by env var
ALLOWED_EMBEDDED_DOMAINS = ["http://localhost:8000","http://localhost:3001","http://localhost:3002"]


# --- Session Cookie Settings ---
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False

# ==============================
# 🖼️ Embedding en iframes
# ==============================
#ALLOW_IFRAME_EMBED = True
#HTTP_HEADERS = {
#    "X-Frame-Options": "ALLOWALL"
#}
TALISMAN_ENABLED = False
ENABLE_PROXY_FIX = True

# ==============================
# 🚀 Feature flags
# ==============================
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "EMBEDDED_SUPERSET_DYNAMIC_PLUGINS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
}

# --- CORS Configuration ---
ENABLE_CORS = True
CORS_OPTIONS = {
  'supports_credentials': True,
  'allow_headers': ['*'],
  'resources':['*'],
  'origins': ALLOWED_EMBEDDED_DOMAINS
}

# ==============================
# 👤 Configuración del rol invitado
# ==============================
GUEST_ROLE_NAME = "Gamma"

# ==============================
# 🔑 Configuración de JWT (para SDK)
# ==============================
EMBEDDED_SUPERSET = {
    "guest_token_jwt_secret": JWT_SECRET,
    "guest_token_jwt_exp_seconds": int(timedelta(hours=1).total_seconds()),
    "allowed_domains": ALLOWED_EMBEDDED_DOMAINS,
}

logger.info("ALLOWED_EMBEDDED_DOMAINS: %s", ALLOWED_EMBEDDED_DOMAINS.split(","))
logger.info("✅ Embedding habilitado con rol %s", GUEST_ROLE_NAME)
