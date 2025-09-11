# superset/superset_config.py
import os
import logging
from datetime import timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("⚡ Config personalizada cargada ⚡")

# ==============================
# 🔑 Claves seguras desde variables de entorno
# ==============================
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY", "default_inseguro_cambiar")
JWT_SECRET = os.getenv("SUPERSET_JWT_SECRET", "jwt_inseguro_cambiar")

# ==============================
# 🖼️ Embedding en iframes
# ==============================
ALLOW_IFRAME_EMBED = True
HTTP_HEADERS = {
    "X-Frame-Options": "ALLOWALL"
}
TALISMAN_ENABLED = False

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
    "allowed_domains": [
        "http://localhost:4200",   # Angular local
    ],
}

logger.info("✅ Embedding habilitado con rol %s", GUEST_ROLE_NAME)
