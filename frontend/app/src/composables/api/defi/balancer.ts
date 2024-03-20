import { fetchExternalAsync } from '@/services/utils';
import { api } from '@/services/rotkehlchen-api';
import type { PendingTask } from '@/types/task';

export function useBalancerApi() {
  const fetchBalancerBalances = (): Promise<PendingTask> => {
    const url = 'blockchains/eth/modules/balancer/balances';
    return fetchExternalAsync(api.instance, url);
  };

  const fetchBalancerEvents = (): Promise<PendingTask> => {
    const url = '/blockchains/eth/modules/balancer/history/events';
    return fetchExternalAsync(api.instance, url);
  };

  return {
    fetchBalancerBalances,
    fetchBalancerEvents,
  };
}
