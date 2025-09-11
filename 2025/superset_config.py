import os
import logging
from datetime import timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("⚡ Config personalizada cargada ⚡")


### IMPRIMIR VARIABLES DE ENTORNO   
logger.info("SUPERSET_DOMAINS_ALLOW: %s", os.environ.get("SUPERSET_DOMAINS_ALLOW", "http://localhost:3002"))
logger.info("SUPERSET_SECRET_KEY: %s",      os.environ.get("SUPERSET_SECRET_KEY", "default_inseguro_cambiar"))
logger.info("SUPERSET_JWT_SECRET: %s",      os.environ.get("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar"))
logger.info("SUPERSET_SQLALCHEMY_DATABASE_URI: %s", os.environ.get("SUPERSET_SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://superset:superset@db:5432/superset"))


# ==============================
# 🔑 Claves seguras desde variables de entorno
# ==============================
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "default_inseguro_cambiar")
JWT_SECRET = os.getenv("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar")
SUPERSET_DOMAINS_ALLOW_TMP = os.getenv("SUPERSET_DOMAINS_ALLOW", "jwt_inseguro_cambiar")
logger.info("SUPERSET_DOMAINS_ALLOW_TMP: %s", SUPERSET_DOMAINS_ALLOW_TMP)

# --- Settings for Embedding & Guest Tokens ---
# ENABLE_EMBEDDED_SUPERSET is controlled by env var

SUPERSET_DOMAINS_ALLOW = os.environ.get("SUPERSET_DOMAINS_ALLOW", "").split("|")
SUPERSET_DOMAINS_ALLOW = [domain.strip() for domain in SUPERSET_DOMAINS_ALLOW if domain.strip()]
if not SUPERSET_DOMAINS_ALLOW:
    SUPERSET_DOMAINS_ALLOW = ["http://localhost:8000","http://localhost:3001","http://localhost:3002"]

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
  'origins': SUPERSET_DOMAINS_ALLOW
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
    "allowed_domains": SUPERSET_DOMAINS_ALLOW,
}

logger.info("SUPERSET_DOMAINS_ALLOW: %s", SUPERSET_DOMAINS_ALLOW)
logger.info("✅ Embedding habilitado con rol %s", GUEST_ROLE_NAME)
