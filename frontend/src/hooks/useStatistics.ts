import {
  StatisticsByTeamOrPlayer,
  StatisticsCategory,
} from '@/types/statistics'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useStatistics(
  statisticsCategory: StatisticsCategory,
  firstTeamId?: number,
  secondTeamId?: number,
) {
  return useQuery({
    queryKey: ['statistics', statisticsCategory, firstTeamId, secondTeamId],
    queryFn: async (): Promise<StatisticsByTeamOrPlayer[]> => {
      let url = `http://localhost:8000/statistics/overview?category=${statisticsCategory}`
      if (firstTeamId && secondTeamId) {
        url = `http://localhost:8000/statistics/overview?category=${statisticsCategory}&versus_team_ids=${firstTeamId}&versus_team_ids=${secondTeamId}`
      }
      const { data } = await axios.get(url)
      return data
    },
  })
}
