import { registerAs } from '@nestjs/config';

export default registerAs('database', () => ({
  type: 'postgres',
  host: process.env.POSTGRES_HOST || 'localhost',
  port: parseInt(process.env.POSTGRES_PORT, 10) || 5432,
  username: process.env.POSTGRES_USER || 'myuser',
  password: process.env.POSTGRES_PASSWORD || 'mypassword',
  database: process.env.POSTGRES_DB || 'mydatabase',
  entities: ['dist/**/*.entity{.ts,.js}'],
  migrations: ['src/migrations/*.ts'],
  synchronize: process.env.NODE_ENV !== 'production',
  logging: process.env.NODE_ENV !== 'production',
}));
