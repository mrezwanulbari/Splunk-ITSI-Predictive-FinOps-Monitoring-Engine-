#!/usr/bin/env python3
"""
ITSI Configuration Backup Script
=================================
Exports ITSI service definitions, KPIs, glass tables,
and notable event policies via the ITSI REST API.

Usage:
    python3 backup_itsi_config.py --host splunk.company.com --token <token> --output /backup/
"""

import argparse
import json
import os
import ssl
import urllib.request
import urllib.parse
from datetime import datetime


class ITSIBackup:
    """Interface to ITSI REST API for configuration backup."""

    ENDPOINTS = {
        'services': '/servicesNS/nobody/SA-ITOA/itoa_interface/service',
        'kpis': '/servicesNS/nobody/SA-ITOA/itoa_interface/kpi_base_search',
        'entities': '/servicesNS/nobody/SA-ITOA/itoa_interface/entity',
        'glass_tables': '/servicesNS/nobody/SA-ITOA/itoa_interface/glass_table',
        'notable_aggregation': '/servicesNS/nobody/SA-ITOA/itoa_interface/notable_event_aggregation_policy',
        'entity_types': '/servicesNS/nobody/SA-ITOA/itoa_interface/entity_type',
    }

    def __init__(self, host, port=8089, token=None):
        self.base_url = f'https://{host}:{port}'
        self.token = token
        self.ssl_ctx = ssl.create_default_context()
        self.ssl_ctx.check_hostname = False
        self.ssl_ctx.verify_mode = ssl.CERT_NONE

    def _get(self, endpoint):
        url = f'{self.base_url}{endpoint}'
        params = urllib.parse.urlencode({'output_mode': 'json', 'count': 0})
        url = f'{url}?{params}'
        req = urllib.request.Request(url)
        req.add_header('Authorization', f'Bearer {self.token}')
        with urllib.request.urlopen(req, context=self.ssl_ctx) as resp:
            return json.loads(resp.read().decode())

    def backup_all(self, output_dir):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(output_dir, f'itsi_backup_{timestamp}')
        os.makedirs(backup_dir, exist_ok=True)

        for name, endpoint in self.ENDPOINTS.items():
            print(f'Backing up {name}...')
            try:
                data = self._get(endpoint)
                filepath = os.path.join(backup_dir, f'{name}.json')
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)
                entries = len(data) if isinstance(data, list) else len(data.get('entry', []))
                print(f'  Saved {entries} {name} to {filepath}')
            except Exception as e:
                print(f'  ERROR backing up {name}: {e}')

        print(f'\nBackup complete: {backup_dir}')
        return backup_dir


def main():
    parser = argparse.ArgumentParser(description='ITSI Configuration Backup')
    parser.add_argument('--host', required=True, help='Splunk host')
    parser.add_argument('--port', default=8089, type=int, help='Management port')
    parser.add_argument('--token', required=True, help='Auth token')
    parser.add_argument('--output', default='./backups', help='Output directory')
    args = parser.parse_args()

    itsi = ITSIBackup(args.host, args.port, args.token)
    itsi.backup_all(args.output)


if __name__ == '__main__':
    main()
