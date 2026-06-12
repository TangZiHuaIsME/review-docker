const express = require('express');
const { Pool } = require('pg');

const app = express();
const port = 3000;

// 数据库连接配置（从环境变量读取）
const pool = new Pool({
  host: process.env.DB_HOST || 'db',      // 数据库主机名，'db' 是 docker-compose 里的服务名
  port: process.env.DB_PORT || 5432,      // PostgreSQL 默认端口
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'postgres',
  database: process.env.DB_NAME || 'mydb',
});

// 测试数据库连接并创建表
async function initDB() {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        created_at TIMESTAMP DEFAULT NOW()
      )
    `);
    await pool.query(`INSERT INTO users (name) VALUES ('Docker用户') ON CONFLICT DO NOTHING`);
    console.log('数据库初始化成功');
  } catch (err) {
    console.error('数据库初始化失败:', err);
  }
}

// API：获取用户列表
app.get('/users', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM users');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// API：添加用户
app.get('/add', async (req, res) => {
  const name = req.query.name || '新用户';
  try {
    await pool.query('INSERT INTO users (name) VALUES ($1)', [name]);
    res.json({ message: `用户 ${name} 添加成功` });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// 启动服务
app.listen(port, () => {
  console.log(`服务运行在 http://localhost:${port}`);
  initDB();
});
