import {
  StatisticsByTeamOrPlayer,
  StatisticsCategory,
} from '@/types/statistics'
import axios from 'axios'
import { useQuery } from 'react-query'

export default function useStatistics(
  statisticsCategory: StatisticsCategory,
  firstTeamId: number,
  secondTeamId: number,
) {
  return useQuery({
    queryKey: ['statistics', statisticsCategory, firstTeamId, secondTeamId],
    queryFn: async (): Promise<StatisticsByTeamOrPlayer[]> => {
      if (firstTeamId && secondTeamId) {
        const { data } = await axios.get(
          `http://localhost:8000/statistics/overview?category=${statisticsCategory}&versus_team_ids=${firstTeamId}&versus_team_ids=${secondTeamId}`,
        )
        return data
      } else {
        const { data } = await axios.get(
          `http://localhost:8000/statistics/overview?category=${statisticsCategory}`,
        )
        return data
      }
    },
  })
}
