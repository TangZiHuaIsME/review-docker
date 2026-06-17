from flask import Flask

app = Flask(__name__)

# ============================================
# 路由1：炫酷新主页（花哨版）
# ============================================
@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps 主页</title>
        <style>
            /* 全局重置与字体 */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                background-size: 400% 400%;
                animation: gradientBG 12s ease infinite;
                padding: 1rem;
            }
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border-radius: 2.5rem;
                padding: 3.5rem 4.5rem;
                max-width: 650px;
                width: 100%;
                text-align: center;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
                border: 1px solid rgba(255, 255, 255, 0.12);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .card:hover {
                transform: scale(1.02) translateY(-5px);
                box-shadow: 0 35px 60px -15px rgba(0, 0, 0, 0.8);
            }

            .icon {
                font-size: 4.5rem;
                margin-bottom: 0.5rem;
                display: inline-block;
                animation: float 3s ease-in-out infinite;
            }
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
                100% { transform: translateY(0px); }
            }

            h1 {
                font-size: 3.8rem;
                font-weight: 700;
                background: linear-gradient(135deg, #f7971e, #ffd200);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                letter-spacing: -0.02em;
                margin-bottom: 0.25rem;
                text-shadow: 0 0 40px rgba(255, 210, 0, 0.15);
            }

            .subtitle {
                font-size: 1.2rem;
                color: rgba(255, 255, 255, 0.7);
                font-weight: 300;
                letter-spacing: 1px;
                margin-bottom: 1.8rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
                padding-bottom: 1.8rem;
            }

            .badge-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 0.8rem;
                margin-bottom: 2.2rem;
            }
            .badge {
                background: rgba(255, 255, 255, 0.06);
                padding: 0.5rem 1.4rem;
                border-radius: 40px;
                font-size: 0.85rem;
                font-weight: 500;
                color: rgba(255, 255, 255, 0.85);
                border: 1px solid rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(4px);
                transition: all 0.2s;
            }
            .badge:hover {
                background: rgba(255, 255, 255, 0.14);
                transform: scale(1.05);
            }

            .status {
                display: inline-flex;
                align-items: center;
                gap: 0.6rem;
                background: rgba(34, 197, 94, 0.15);
                padding: 0.55rem 1.8rem;
                border-radius: 60px;
                color: #86efac;
                font-size: 0.95rem;
                font-weight: 500;
                border: 1px solid rgba(34, 197, 94, 0.2);
                backdrop-filter: blur(4px);
                transition: all 0.3s;
            }
            .status:hover {
                background: rgba(34, 197, 94, 0.25);
                box-shadow: 0 0 20px rgba(34, 197, 94, 0.15);
            }
            .status-dot {
                width: 10px;
                height: 10px;
                border-radius: 50%;
                background: #22c55e;
                display: inline-block;
                animation: pulse-dot 2s infinite;
            }
            @keyframes pulse-dot {
                0% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.4; transform: scale(0.7); }
                100% { opacity: 1; transform: scale(1); }
            }

            .footer {
                margin-top: 2.5rem;
                font-size: 0.8rem;
                color: rgba(255, 255, 255, 0.25);
                letter-spacing: 0.5px;
            }
            .footer span {
                color: rgba(255, 255, 255, 0.4);
            }

            /* 响应式 */
            @media (max-width: 520px) {
                .card {
                    padding: 2.2rem 1.8rem;
                }
                h1 {
                    font-size: 2.6rem;
                }
                .icon {
                    font-size: 3.2rem;
                }
                .subtitle {
                    font-size: 1rem;
                }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="icon">🚀</div>
            <h1>Hello, DevOps!</h1>   <!-- 原始代码的“Hello, DevOps!”被保留在这里 -->
            <p class="subtitle">✨ 自动化 · 可观测 · 弹性 ✨</p>

            <div class="badge-container">
                <span class="badge">🐍 Flask</span>
                <span class="badge">🐳 Docker</span>
                <span class="badge">☁️ AWS</span>
                <span class="badge">🔁 CI/CD</span>
            </div>

            <div class="status">
                <span class="status-dot"></span>
                系统运行中 · 一切正常
            </div>

            <div class="footer">
                <span>© 2026 DevOps 实战 · 版本 v3.1</span>
            </div>
        </div>
    </body>
    </html>
    '''


# ============================================
# 路由2：原始极简版（保留原始代码，备用）
# ============================================
@app.route('/classic')
def classic():
    # 这是你最初的 Hello World 代码，完整保留！
    return "<h1>Hello, DevOps!</h1>"


# ============================================
# 路由3：健康检查
# ============================================
@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
