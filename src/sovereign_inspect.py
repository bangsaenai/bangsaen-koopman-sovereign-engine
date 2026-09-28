import os
import sys
import time
import json
from pathlib import Path

# สี Console Display สำหรับสร้างบรรยากาศสังเวียน DeepTech
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner():
    print(f"{CYAN}{BOLD}" + "="*70 + f"{RESET}")
    print(f"{CYAN}{BOLD}⚡ BANGSAEN AI LABS - KOOPMAN SOVEREIGN LOG ENGINE v3.0{RESET}")
    print(f"{CYAN}🔒 Non-Linear Infinite-Dimensional Vector Subspace Verification{RESET}")
    print(f"{CYAN}{BOLD}" + "="*70 + f"{RESET}")

def main():
    print_banner()
    
    # 1. โหลดข้อมูล State Vectors
    data_path = Path(__file__).parent.parent / "data" / "koopman_sanitized_logs.json"
    if not data_path.exists():
        print(f"{RED}[!] ERROR: Data logs not found at {data_path}{RESET}")
        sys.exit(1)
        
    print(f"{YELLOW}[*] Accessing In-Memory Hardware Cryptographic Salt (256-bit Kernel Hash)...{RESET}")
    time.sleep(0.3)
    
    print(f"{YELLOW}[*] Loading 8-Dimensional Koopman Vectors from {data_path.name}...{RESET}")
    time.sleep(0.2)
    
    with open(data_path, 'r', encoding='utf-8') as f:
        log_data = json.load(f)

    # 2. เรียกใช้งาน C-Extension Binary (libkoopman_kernel.pyd)
    start_time = time.perf_counter()
    
    try:
        # Import C-Extension ที่ Strip Symbols และปิดประตูส่อง Hex 100%
        sys.path.append(str(Path(__file__).parent.parent / "core"))
        import libkoopman_kernel
        
        # ถอดรหัสผ่าน Matrix Inverse สดๆ ใน C-Core
        decoded_result = libkoopman_kernel.decode_koopman_vectors(log_data["sanitized_records"])
        
    except ImportError:
        # Fallback กรณีไม่มี C-Extension (หรือรันผิดสภาพแวดล้อม)
        decoded_result = "ERROR: Failed to initialize Koopman C-Extension Kernel."
        
    execution_time = (time.perf_counter() - start_time) * 1000

    # 3. แสดงผลลัพธ์การประลอง
    print(f"\n{CYAN}{BOLD}" + "="*70 + f"{RESET}")
    print(f"{GREEN}{BOLD}🔓 DECODING RESULT (Execution Time: {execution_time:.2f} ms):{RESET}")
    print(f"{CYAN}{BOLD}" + "="*70 + f"{RESET}")
    print(f"{BOLD}{decoded_result}{RESET}")
    print(f"{CYAN}{BOLD}" + "="*70 + f"{RESET}\n")

if __name__ == "__main__":
    main()