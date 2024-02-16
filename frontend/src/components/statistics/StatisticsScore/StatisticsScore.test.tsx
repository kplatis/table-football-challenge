import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import StatisticsScore from '../StatisticsScore'
import { mockTeams } from '@/__tests__/mockData/teams'
import Providers from '@/components/Providers'
import { mockStatistics } from '@/__tests__/mockData/statistics'

describe('StatisticsScore', () => {
  test('renders loader when data is loading', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: null,
      }))

    render(
      <Providers>
        <StatisticsScore firstTeam={mockTeams[0]} secondTeam={mockTeams[1]} />
      </Providers>,
    )

    // Check if loader is rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders correct statistics when data is loaded', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockStatistics,
      }))

    render(
      <Providers>
        <StatisticsScore firstTeam={mockTeams[0]} secondTeam={mockTeams[1]} />
      </Providers>,
    )

    // Check if correct statistics sentence is rendered
    expect(
      screen.getByText(
        'team1 loses in direct confrontations with team2: 2 - 3',
      ),
    ).toBeInTheDocument()
  })

  test('renders correct message when there are no games between teams', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: [],
      }))

    render(
      <Providers>
        <StatisticsScore firstTeam={mockTeams[0]} secondTeam={mockTeams[1]} />
      </Providers>,
    )

    // Check if correct message is rendered
    expect(
      screen.getByText('There are no games between the two teams'),
    ).toBeInTheDocument()
  })
})
