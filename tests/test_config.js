const fs = require('fs');
const path = require('path');

test('database-config.json exists', () => {
  const filePath = path.join(__dirname, '../config/database-config.json');
  expect(fs.existsSync(filePath)).toBe(true);
});

test('deployment-settings.ini exists', () => {
  const filePath = path.join(__dirname, '../config/deployment-settings.ini');
  expect(fs.existsSync(filePath)).toBe(true);
});
