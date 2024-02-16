import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import StatisticsTable from '../StatisticsTable'
import Providers from '@/components/Providers'
import { StatisticsCategory } from '@/types/statistics'
import { mockStatistics } from '@/__tests__/mockData/statistics'

// Mock useStatistics hook
jest.mock('@/hooks/useStatistics')

describe('StatisticsTable', () => {
  test('renders loader when data is loading', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: true,
        data: null,
      }))

    render(
      <Providers>
        <StatisticsTable category={StatisticsCategory.All} />
      </Providers>,
    )

    // Check if loader is rendered
    expect(screen.getByTestId('loader')).toBeInTheDocument()
  })

  test('renders table with correct data when data is loaded', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: mockStatistics,
      }))

    render(
      <Providers>
        <StatisticsTable category={StatisticsCategory.Teams} />
      </Providers>,
    )
    // Check if table headers are rendered
    expect(screen.getByText('Name')).toBeInTheDocument()
    expect(screen.getByText('Wins')).toBeInTheDocument()
    expect(screen.getByText('Losses')).toBeInTheDocument()
    expect(screen.getByText('Win Ratio')).toBeInTheDocument()
    expect(screen.getByText('Goals For')).toBeInTheDocument()
    expect(screen.getByText('Goals Against')).toBeInTheDocument()
    expect(screen.getByText('Goals Difference')).toBeInTheDocument()
    // table show have 3 rows (header + 2 stats)
    expect(screen.getAllByRole('row')).toHaveLength(3)
  })

  test('renders nothing when data is not available', () => {
    jest
      .spyOn(require('@/hooks/useStatistics'), 'default')
      .mockImplementation(() => ({
        isLoading: false,
        data: [],
      }))

    render(
      <Providers>
        <StatisticsTable category={StatisticsCategory.Teams} />
      </Providers>,
    )

    // Check if nothing is rendered
    expect(screen.queryByTestId('statistics-table')).toBeNull()
  })
})
