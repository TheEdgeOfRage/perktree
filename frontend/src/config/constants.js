const API_ROUTE = '/api';

const ENVIRONMENTS = {
	'perktree.localhost': 'dev',
	'perktree.theedgeofrage.com': 'prod',
};

const BACKEND_HOSTNAMES = {
	dev: 'http://localhost:8001',
	prod: 'https://perktree.theedgeofrage.com',
};

export { API_ROUTE, ENVIRONMENTS, BACKEND_HOSTNAMES };

