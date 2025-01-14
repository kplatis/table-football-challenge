/*eslint-env node*/
module.exports = {
    roots: ['<rootDir>/src'],  
    testEnvironment: 'jsdom',
    testMatch: [
        '<rootDir>/src/components/**/*.{spec,test}.{ts,tsx}', 
      ],
      transform: {
        '^.+\\.(ts|tsx)$': 'ts-jest', // Transform .ts and .tsx files with ts-jest
      },
    verbose: true,
    transformIgnorePatterns: ['<rootDir>/node_modules/'],
    moduleDirectories: ['node_modules', '<rootDir>/'],    
    moduleNameMapper: {
      '^@/(.*)$': '<rootDir>/src/$1',
      "\\.css$": "identity-obj-proxy",
    },
    globals: {
      "ts-jest": {
        "tsconfig": "./tsconfig.spec.json"
      }
    },
    setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  };
  