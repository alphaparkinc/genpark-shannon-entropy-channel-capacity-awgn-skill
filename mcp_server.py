import sys
import json
from client import ShannonChannelAnalyzer

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-shannon-entropy-channel-capacity-awgn-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_channel_capacity",
                        "description": "Calculate theoretical channel capacity limits for AWGN, BSC, or BEC channels",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "bandwidth_hz": {"type": "number", "default": 1000.0},
                                "snr_linear": {"type": "number", "default": 15.0},
                                "bsc_error_prob": {"type": "number", "default": 0.05}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "compute_channel_capacity":
            b = args.get("bandwidth_hz", 1000.0)
            snr = args.get("snr_linear", 15.0)
            p = args.get("bsc_error_prob", 0.05)
            awgn_cap = ShannonChannelAnalyzer.shannon_hartley_capacity(b, snr)
            bsc_cap = ShannonChannelAnalyzer.bsc_capacity(p)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps({"awgn_capacity_bps": awgn_cap, "bsc_capacity_bits": bsc_cap})}]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
