import datetime
import logging

logger = logging.getLogger(__name__)

class MemoryBank:
    def __init__(self):
        self.sessions = {}
        self.long_term_memory = {}
        self.interaction_log = []
        logger.info("MemoryBank initialized")

    def create_session(self, patient_id, initial_data):
        session_id = f"{patient_id}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.sessions[session_id] = {
            "patient_id": patient_id,
            "created_at": datetime.datetime.now().isoformat(),
            "data": initial_data,
            "interactions": []
        }
        return session_id

    def update_session(self, session_id, interaction):
        if session_id in self.sessions:
            self.sessions[session_id]["interactions"].append({
                "timestamp": datetime.datetime.now().isoformat(),
                "data": interaction
            })

    def store_long_term(self, patient_id, data):
        self.long_term_memory.setdefault(patient_id, []).append({
            "timestamp": datetime.datetime.now().isoformat(),
            "data": data
        })
