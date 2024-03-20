import { fetchExternalAsync } from '@/services/utils';
import { api } from '@/services/rotkehlchen-api';
import { ProtocolVersion } from '@/types/defi';
import type { PendingTask } from '@/types/task';

export function useYearnApi() {
  const fetchYearnVaultsHistory = (
    protocolVersion: ProtocolVersion = ProtocolVersion.V1,
  ): Promise<PendingTask> => {
    const path = protocolVersion === ProtocolVersion.V1 ? 'vaults' : 'vaultsv2';
    const url = `/blockchains/eth/modules/yearn/${path}/history`;
    return fetchExternalAsync(api.instance, url);
  };

  const fetchYearnVaultsBalances = (
    protocolVersion: ProtocolVersion = ProtocolVersion.V1,
  ): Promise<PendingTask> => {
    const path = protocolVersion === ProtocolVersion.V1 ? 'vaults' : 'vaultsv2';
    const url = `/blockchains/eth/modules/yearn/${path}/balances`;
    return fetchExternalAsync(api.instance, url);
  };

  return {
    fetchYearnVaultsHistory,
    fetchYearnVaultsBalances,
  };
}
