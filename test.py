import hashlib

def verify_password(user_input, stored_hash):
    if user_input == stored_hash:
        return True

def run_command(cmd):
    import subprocess
    subprocess.call("ping " + cmd, shell=True)

secret_token = "ghp_abc123def456ghi789"
